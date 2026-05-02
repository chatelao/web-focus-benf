import os
import sys
import subprocess
import datetime
import argparse
import re

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

def post_process_xhtml(filepath):
    """Injects custom CSS into the generated XHTML to match Oracle style."""
    print(f"Post-processing {filepath} for Oracle styling...")
    with open(filepath, "r") as f:
        content = f.read()

    # Define Oracle-inspired style overrides
    oracle_styles = """
    /* Oracle Style Overrides */
    .line                 { stroke: #444444 !important; stroke-width: 1.5 !important; }
    .bold-line            { stroke: #222222 !important; stroke-width: 2 !important; }
    .filled               { fill: #444444 !important; }
    rect.terminal         { fill: #eef4ff !important; stroke: #002b80 !important; stroke-width: 1.5 !important; }
    rect.nonterminal      { fill: #ffffff !important; stroke: #444444 !important; stroke-width: 1.5 !important; }
    text.terminal         { fill: #002b80 !important; font-weight: bold !important; font-family: 'Verdana', sans-serif !important; }
    text.nonterminal      { fill: #222222 !important; font-family: 'Verdana', sans-serif !important; }

    /* Navigation Bar */
    .nav-bar {
        background-color: #002b80;
        padding: 10px 20px;
        margin-bottom: 20px;
        border-radius: 4px;
        font-family: 'Verdana', sans-serif;
    }
    .nav-bar a {
        color: #ffffff;
        text-decoration: none;
        font-weight: bold;
    }
    .nav-bar a:hover {
        text-decoration: underline;
    }
    """

    # The RR tool embeds CSS in every SVG. We'll append our overrides to the main head style block
    # and also use !important to ensure they take precedence.
    if "</style>" in content:
        # Insert into the first style block in the head
        content = content.replace("</style>", oracle_styles + "  </style>", 1)

    # Inject navigation bar at the beginning of body
    nav_bar_html = '<div class="nav-bar"><a href="index.html">&larr; Back to Index</a></div>'
    content = content.replace("<body>", f"<body>\n      {nav_bar_html}", 1)

    with open(filepath, "w") as f:
        f.write(content)
        if not content.endswith('\n'):
            f.write('\n')

def generate_docs(grammars=None, output_dir="docs", ebnf_dir="build/ebnf", color="#4D88FF", width=None,
                  suppress_ebnf=False, offset=None, force=False):
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
        rr.generate(ebnf_path, out_path=xhtml_path, color=color, width=width,
                    suppress_ebnf=suppress_ebnf, offset=offset)

        post_process_xhtml(xhtml_path)
        validate_output(xhtml_path)
        generated_files.append((grammar_name, xhtml_name))

    generate_index(output_dir, generated_files)

def generate_index(output_dir, files):
    """Generates an index.html file linking to all railroad diagrams."""
    index_path = os.path.join(output_dir, "index.html")
    print(f"Generating Index at {index_path}...")

    links = "".join([f'<li><a href="{path}">{name}</a></li>' for name, path in files])
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>WebFocus Syntax Railroad Diagrams</title>
    <style>
        body {{ font-family: sans-serif; margin: 40px; background-color: #f0f5ff; }}
        h1 {{ color: #002b80; }}
        .metadata {{ color: #666; font-size: 0.9em; margin-bottom: 20px; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; }}
        a {{ text-decoration: none; color: #4D88FF; font-weight: bold; font-size: 1.2em; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>WebFocus Syntax Railroad Diagrams</h1>
    <p>Visual representation of the WebFocus grammars.</p>
    <div class="metadata">Generated on: {now}</div>
    <ul>
        {links}
    </ul>
</body>
</html>
"""
    with open(index_path, "w") as f:
        f.write(html_content)
        if not html_content.endswith('\n'):
            f.write('\n')
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
    parser.add_argument('--suppress-ebnf', action='store_true', help='Do not show EBNF next to generated diagrams')
    parser.add_argument('--offset', type=int, help='Hue offset to secondary color in degrees')
    parser.add_argument('--force', '-f', action='store_true', help='Force regeneration of all diagrams')

    args = parser.parse_args()

    generate_docs(
        grammars=args.grammars,
        output_dir=args.output_dir,
        ebnf_dir=args.ebnf_dir,
        color=args.color,
        width=args.width,
        suppress_ebnf=args.suppress_ebnf,
        offset=args.offset,
        force=args.force
    )
