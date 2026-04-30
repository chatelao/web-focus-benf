import os
import sys
import subprocess

# Add src to sys.path to find rr_wrapper
sys.path.append(os.path.join(os.getcwd(), "src"))
from rr_wrapper import RRTool

def generate_docs():
    src_dir = "src"
    docs_dir = "docs"
    ebnf_dir = "build/ebnf"

    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(ebnf_dir, exist_ok=True)

    grammars = ["WebFocusReport.g4", "MasterFile.g4"]

    rr = RRTool()

    for grammar in grammars:
        grammar_path = os.path.join(src_dir, grammar)
        ebnf_path = os.path.join(ebnf_dir, grammar.replace(".g4", ".ebnf"))
        xhtml_path = os.path.join(docs_dir, grammar.replace(".g4", ".xhtml"))

        print(f"Generating EBNF for {grammar}...")
        with open(ebnf_path, "w") as f:
            subprocess.run(["python3", "scripts/antlr4_to_ebnf.py", grammar_path, "--check"], stdout=f, check=True)

        print(f"Generating Railroad Diagram for {grammar}...")
        rr.generate(ebnf_path, out_path=xhtml_path, color="#4D88FF")

if __name__ == "__main__":
    generate_docs()
