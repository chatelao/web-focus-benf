import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from wf_parser import WebFocusParser

def main():
    fex_path = 'test/documentation_examples/project4_data_merge/data_merge.fex'
    with open(fex_path, 'r') as f:
        code = f.read()

    parser = WebFocusParser()
    try:
        tree = parser.parse(code)
        print("Successfully parsed data_merge.fex")
    except Exception as e:
        print(f"Failed to parse data_merge.fex: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
