import os
import sys
import subprocess
import argparse

# Add src to sys.path to find rr_wrapper
sys.path.append(os.path.join(os.getcwd(), "src"))
try:
    from rr_wrapper import RRTool
except ImportError:
    # Handle the case where the script might be run from a different directory
    sys.path.append(os.getcwd())
    from src.rr_wrapper import RRTool

def is_up_to_date(source_path, target_path):
    """Returns True if the target file exists and is newer than the source file."""
    if not os.path.exists(target_path):
        return False
    return os.path.getmtime(target_path) > os.path.getmtime(source_path)

def generate_docs(grammars=None, output_dir="docs", ebnf_dir="build/ebnf", color="#4D88FF", width=None, force=False):
    src_dir = "src"

    if not grammars:
        grammars = ["WebFocusReport.g4", "MasterFile.g4"]

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(ebnf_dir, exist_ok=True)

    rr = RRTool()

    generated_files = []

    for grammar in grammars:
        # If grammar is just a name, assume it's in src/
        if not os.path.exists(grammar):
            grammar_path = os.path.join(src_dir, grammar)
        else:
            grammar_path = grammar

        grammar_name = os.path.basename(grammar_path)
        ebnf_path = os.path.join(ebnf_dir, grammar_name.replace(".g4", ".ebnf"))
        xhtml_name = grammar_name.replace(".g4", ".xhtml")
        xhtml_path = os.path.join(output_dir, xhtml_name)

        if not force and is_up_to_date(grammar_path, xhtml_path):
            print(f"Skipping {grammar_name} (already up-to-date).")
            generated_files.append((grammar_name, xhtml_name))
            continue

        print(f"Generating EBNF for {grammar_name}...")
        with open(ebnf_path, "w") as f:
            # We assume scripts/antlr4_to_ebnf.py exists and is in the current working directory or relative to it.
            subprocess.run(["python3", "scripts/antlr4_to_ebnf.py", grammar_path, "--check"], stdout=f, check=True)

        print(f"Generating Railroad Diagram for {grammar_name}...")
        rr.generate(ebnf_path, out_path=xhtml_path, color=color, width=width)

        validate_output(xhtml_path)
        generated_files.append((grammar_name, xhtml_name))

    generate_index(output_dir, generated_files)

def generate_index(output_dir, files):
    """Generates an index.html file linking to all railroad diagrams."""
    index_path = os.path.join(output_dir, "index.html")
    print(f"Generating Index at {index_path}...")

    links = "".join([f'<li><a href="{path}">{name}</a></li>' for name, path in files])

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>WebFocus Syntax Railroad Diagrams</title>
    <style>
        body {{ font-family: sans-serif; margin: 40px; background-color: #f0f5ff; }}
        h1 {{ color: #002b80; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; }}
        a {{ text-decoration: none; color: #4D88FF; font-weight: bold; font-size: 1.2em; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>WebFocus Syntax Railroad Diagrams</h1>
    <p>Visual representation of the WebFocus grammars.</p>
    <ul>
        {links}
    </ul>
</body>
</html>
"""
    with open(index_path, "w") as f:
        f.write(html_content)
    print(f"Verified: {index_path} is valid.")

def validate_output(filepath):
    """Verifies that the generated file exists, is non-empty, and contains SVG content."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Verification failed: {filepath} was not generated.")

    if os.path.getsize(filepath) == 0:
        raise ValueError(f"Verification failed: {filepath} is empty.")

    with open(filepath, "r") as f:
        content = f.read()
        if "<svg" not in content:
            raise ValueError(f"Verification failed: {filepath} does not contain SVG content.")

    print(f"Verified: {filepath} is valid.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Orchestrate railroad diagram generation.')
    parser.add_argument('--grammars', nargs='+', help='List of grammar files to process (e.g. WebFocusReport.g4)')
    parser.add_argument('--output-dir', default='docs', help='Directory for generated diagrams (default: docs)')
    parser.add_argument('--ebnf-dir', default='build/ebnf', help='Directory for intermediate EBNF files (default: build/ebnf)')
    parser.add_argument('--color', default='#4D88FF', help='Base color for diagrams (default: #4D88FF)')
    parser.add_argument('--width', type=int, help='Try to break graphics into multiple lines if width exceeds this value')
    parser.add_argument('--force', '-f', action='store_true', help='Force regeneration of all diagrams')

    args = parser.parse_args()

    generate_docs(
        grammars=args.grammars,
        output_dir=args.output_dir,
        ebnf_dir=args.ebnf_dir,
        color=args.color,
        width=args.width,
        force=args.force
    )
