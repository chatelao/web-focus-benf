import re
import sys

def convert_antlr_to_ebnf(antlr_content):
    """
    Converts ANTLR4 grammar content to W3C EBNF.
    This is an initial implementation focusing on basic rule mapping.
    """
    # Remove comments but skip strings
    antlr_content = remove_comments(antlr_content)

    # Extract parser rules (start with lowercase)
    # Using a more robust regex that handles multiline rules and leading whitespace
    parser_rules = re.findall(r'^\s*([a-z]\w*)\s*:\s*(.*?)\s*;', antlr_content, re.DOTALL | re.MULTILINE)

    # Extract lexer rules (start with uppercase)
    lexer_rules = re.findall(r'^\s*([A-Z]\w*)\s*:\s*(.*?)\s*;', antlr_content, re.DOTALL | re.MULTILINE)

    ebnf_rules = []

    for rule_name, body in parser_rules:
        body = format_body(body)
        ebnf_rules.append(f"{rule_name} ::= {body}")

    for rule_name, body in lexer_rules:
        body = format_body(body)
        ebnf_rules.append(f"{rule_name} ::= {body}")

    return "\n".join(ebnf_rules)

def remove_comments(content):
    """
    Removes ANTLR4 comments while preserving strings.
    """
    # Regex to match single-quoted strings, double-quoted strings,
    # block comments, or line comments.
    # Fixed: non-greedy match for //.* to avoid swallowing the whole line if multiple comments exist
    # and to not swallow \n which might be needed for ^ anchors in rules.
    pattern = r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"|/\*.*?\*/|//[^\n]*"

    def replace(match):
        m = match.group(0)
        if m.startswith('/') :
            return ' ' # It's a comment, replace with space
        return m # It's a string, keep it

    return re.sub(pattern, replace, content, flags=re.DOTALL)

def format_body(body):
    """
    Formats the body of a rule for W3C EBNF.
    """
    # Remove ANTLR actions if any
    body = re.sub(r'\{.*?\}', '', body, flags=re.DOTALL)

    # Clean up whitespace
    body = body.replace('\n', ' ').strip()
    body = re.sub(r'\s+', ' ', body)

    return body

if __name__ == "__main__":
    if len(sys.argv) < 2:
        content = sys.stdin.read()
    else:
        with open(sys.argv[1], 'r') as f:
            content = f.read()

    print(convert_antlr_to_ebnf(content))
