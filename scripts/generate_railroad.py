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

def post_process_xhtml(filepath, metadata=None):
    """Injects custom CSS and JS into the generated XHTML to match Oracle style and add filtering."""
    print(f"Post-processing {filepath} for Oracle styling and filtering...")
    with open(filepath, "r") as f:
        content = f.read()

    metadata = metadata or {}

    # Define Oracle-inspired style overrides
    oracle_styles = """
    /* Oracle Style Overrides */
    body {
        margin: 0;
        padding: 0;
        background-color: #f0f5ff;
    }
    .line                 { stroke: #444444 !important; stroke-width: 1.5 !important; }
    .bold-line            { stroke: #222222 !important; stroke-width: 2 !important; }
    .filled               { fill: #444444 !important; }
    rect.terminal         { fill: #eef4ff !important; stroke: #002b80 !important; stroke-width: 1.5 !important; }
    rect.nonterminal      { fill: #ffffff !important; stroke: #444444 !important; stroke-width: 1.5 !important; }
    text.terminal         { fill: #002b80 !important; font-weight: bold !important; font-family: 'Verdana', sans-serif !important; }
    text.nonterminal      { fill: #222222 !important; font-family: 'Verdana', sans-serif !important; }

    /* Navigation Bar */
    .nav-bar {
        position: sticky;
        top: 0;
        z-index: 1000;
        background-color: #002b80;
        padding: 10px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-family: 'Verdana', sans-serif;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .nav-bar a {
        color: #ffffff;
        text-decoration: none;
        font-weight: bold;
    }
    .nav-bar a:hover {
        text-decoration: underline;
    }
    .search-container {
        display: flex;
        align-items: center;
    }
    #rule-search {
        padding: 5px 10px;
        border-radius: 4px;
        border: 1px solid #ccc;
        font-size: 14px;
        width: 250px;
    }

    /* Content Layout */
    .content-area {
        padding: 20px;
    }
    .rule-container {
        background-color: #ffffff;
        border: 1px solid #d0d7de;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .rule-container:hover {
        border-color: #002b80;
    }
    .rule-container:target {
        border: 2px solid #002b80;
        background-color: #f8faff;
        scroll-margin-top: 70px;
    }

    /* Clickable non-terminals */
    a[xlink|href], a[href] {
        cursor: pointer;
    }
    a:hover rect.nonterminal {
        fill: #f0f5ff !important;
        stroke: #002b80 !important;
    }
    a:active rect.nonterminal {
        fill: #eef4ff !important;
    }
    a:hover text.nonterminal {
        fill: #002b80 !important;
        text-decoration: underline;
    }

    #result-count {
        color: #ffffff;
        font-size: 14px;
        margin-right: 15px;
    }
    #clear-search {
        background-color: #4D88FF;
        color: white;
        border: none;
        padding: 5px 10px;
        border-radius: 4px;
        cursor: pointer;
        margin-left: 10px;
        font-size: 14px;
    }
    #clear-search:hover {
        background-color: #3b6edb;
    }
    """

    # Wrap rules in containers for filtering
    content = wrap_rules_in_containers(content, metadata)

    # Ensure links work correctly in XHTML by potentially adding the xlink namespace if missing
    if 'xmlns:xlink="http://www.w3.org/1999/xlink"' not in content:
        content = content.replace('<svg ', '<svg xmlns:xlink="http://www.w3.org/1999/xlink" ', 1)

    # Add styling for rule descriptions
    oracle_styles += """
    .rule-description {
        font-style: italic;
        color: #555;
        margin-top: 5px;
        margin-bottom: 15px;
        font-family: 'Verdana', sans-serif;
        font-size: 13px;
        line-height: 1.4;
        border-left: 3px solid #002b80;
        padding-left: 10px;
    }
    """

    # The RR tool embeds CSS in every SVG. We'll append our overrides to the main head style block
    # and also use !important to ensure they take precedence.
    if "</style>" in content:
        # Insert into the first style block in the head
        content = content.replace("</style>", oracle_styles + "  </style>", 1)

    # Inject navigation bar at the beginning of body
    nav_bar_html = '''<div class="nav-bar">
        <a href="index.html">&larr; Back to Index</a>
        <div class="search-container">
            <span id="result-count"></span>
            <input type="text" id="rule-search" placeholder="Search rules..." />
            <button id="clear-search">Clear</button>
        </div>
    </div>'''
    content = content.replace("<body>", f"<body>\n      {nav_bar_html}", 1)

    # Inject JS for filtering before </body>
    filter_js = """
    <script type="text/javascript">
    document.addEventListener('DOMContentLoaded', function() {
        const searchInput = document.getElementById('rule-search');
        const clearButton = document.getElementById('clear-search');
        const resultCount = document.getElementById('result-count');
        const containers = document.querySelectorAll('.rule-container');

        function updateFilter() {
            const query = searchInput.value.toLowerCase();
            let visibleCount = 0;
            containers.forEach(container => {
                const ruleName = container.getAttribute('data-rule').toLowerCase();
                if (ruleName.includes(query)) {
                    container.style.display = 'block';
                    visibleCount++;
                } else {
                    container.style.display = 'none';
                }
            });
            resultCount.textContent = `${visibleCount} rules found`;
        }

        searchInput.addEventListener('input', updateFilter);

        clearButton.addEventListener('click', function() {
            searchInput.value = '';
            updateFilter();
            searchInput.focus();
        });

        function handleHashChange() {
            if (window.location.hash) {
                const hash = window.location.hash.substring(1);
                const target = document.getElementById(hash);
                if (target) {
                    // When a rule is targeted, we should clear the search to make sure it's visible
                    if (searchInput.value !== '') {
                        searchInput.value = '';
                        updateFilter();
                    }
                    target.style.display = 'block';
                    target.scrollIntoView();
                }
            }
        }

        window.addEventListener('hashchange', handleHashChange);

        // Initial setup
        updateFilter();
        handleHashChange();
    });
    </script>
    """
    content = content.replace("</body>", f"{filter_js}\n   </body>")

    with open(filepath, "w") as f:
        f.write(content)
        if not content.endswith('\n'):
            f.write('\n')

def wrap_rules_in_containers(content, metadata):
    """Wraps each rule into a div for better layout and filtering."""
    # Find all rule starts. RR tool uses a specific pattern for rule headers.
    rule_pattern = re.compile(r'<xhtml:p [^>]*style="font-size: 14px; font-weight:bold"><xhtml:a name="([^"]+)">.*?</xhtml:p>')

    matches = list(rule_pattern.finditer(content))
    if not matches:
        return content

    new_content = content[:matches[0].start()]
    new_content += '<div class="content-area">\n'

    # Try to find the start of the signature to know where to stop
    sig_marker = '<xhtml:table border="0" class="signature">'
    sig_table_pos = content.find(sig_marker)
    if sig_table_pos != -1:
        # The signature table is usually inside an xhtml:p. Let's find the opening of that p.
        p_start = content.rfind('<xhtml:p', 0, sig_table_pos)
        if p_start != -1 and sig_table_pos - p_start < 500: # Sanity check for proximity
            sig_start = p_start
        else:
            sig_start = sig_table_pos
    else:
        sig_start = content.find('</body>')

    for i in range(len(matches)):
        start = matches[i].start()
        if i + 1 < len(matches):
            end = matches[i+1].start()
        else:
            end = sig_start

        rule_name = matches[i].group(1)
        rule_body = content[start:end]

        # Clean up some separators to avoid double spacing in containers
        rule_body = rule_body.replace('<xhtml:br xmlns:xhtml="http://www.w3.org/1999/xhtml" />', '')
        rule_body = rule_body.replace('<xhtml:hr xmlns:xhtml="http://www.w3.org/1999/xhtml" />', '')

        new_content += f'   <div class="rule-container" id="{rule_name}" data-rule="{rule_name}">\n'

        description = metadata.get(rule_name)
        if description:
            # Escape HTML in description and convert newlines to <br/>
            import html
            safe_desc = html.escape(description).replace('\n', '<br/>')
            new_content += f'      <div class="rule-description">{safe_desc}</div>\n'

        new_content += f'      {rule_body.strip()}\n'
        new_content += '   </div>\n'

    new_content += '</div>\n'
    new_content += content[sig_start:]
    return new_content

def generate_docs(grammars=None, output_dir="docs", ebnf_dir="build/ebnf", metadata_dir="build/metadata",
                  color="#4D88FF", width=None, suppress_ebnf=False, offset=None, force=False):
    src_dir = "src"

    if not grammars:
        grammars = ["WebFocusReport.g4", "MasterFile.g4"]

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(ebnf_dir, exist_ok=True)
    os.makedirs(metadata_dir, exist_ok=True)

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
        metadata_path = os.path.join(metadata_dir, grammar_name.replace(".g4", ".json"))
        xhtml_name = grammar_name.replace(".g4", ".xhtml")
        xhtml_path = os.path.join(output_dir, xhtml_name)

        if not force and is_up_to_date(grammar_path, xhtml_path):
            print(f"Skipping {grammar_name} (already up-to-date).")
            generated_files.append((grammar_name, xhtml_name))
            continue

        print(f"Generating EBNF and Metadata for {grammar_name}...")
        with open(ebnf_path, "w") as f:
            # We assume scripts/antlr4_to_ebnf.py exists and is in the current working directory or relative to it.
            subprocess.run(["python3", "scripts/antlr4_to_ebnf.py", grammar_path, "--check", "--metadata", metadata_path], stdout=f, check=True)

        print(f"Generating Railroad Diagram for {grammar_name}...")
        rr.generate(ebnf_path, out_path=xhtml_path, color=color, width=width,
                    suppress_ebnf=suppress_ebnf, offset=offset)

        metadata = {}
        if os.path.exists(metadata_path):
            import json
            with open(metadata_path, "r") as f:
                metadata = json.load(f)

        post_process_xhtml(xhtml_path, metadata=metadata)
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
    parser.add_argument('--metadata-dir', default='build/metadata', help='Directory for intermediate metadata files (default: build/metadata)')
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
        metadata_dir=args.metadata_dir,
        color=args.color,
        width=args.width,
        suppress_ebnf=args.suppress_ebnf,
        offset=args.offset,
        force=args.force
    )
