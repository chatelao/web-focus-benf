import re
import sys

def convert_antlr_to_ebnf(antlr_content):
    """
    Converts ANTLR4 grammar content to W3C EBNF.
    """
    # Remove comments but skip strings
    antlr_content = remove_comments(antlr_content)

    # Extract parser rules (start with lowercase)
    parser_rules = re.findall(r'^\s*([a-z]\w*)\s*:\s*(.*?)\s*;', antlr_content, re.DOTALL | re.MULTILINE)

    # Extract lexer rules (start with uppercase)
    lexer_rules = re.findall(r'^\s*(fragment\s+)?([A-Z]\w*)\s*:\s*(.*?)\s*;', antlr_content, re.DOTALL | re.MULTILINE)

    ebnf_rules = []

    for rule_name, body in parser_rules:
        body = format_body(body)
        ebnf_rules.append(f"{rule_name} ::= {body}")

    for fragment, rule_name, body in lexer_rules:
        body = format_body(body, is_lexer=True)
        ebnf_rules.append(f"{rule_name} ::= {body}")

    return "\n".join(ebnf_rules)

def remove_comments(content):
    """
    Removes ANTLR4 comments while preserving strings.
    """
    pattern = r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"|/\*.*?\*/|//[^\n]*"

    def replace(match):
        m = match.group(0)
        if m.startswith('/') :
            return ' '
        return m

    return re.sub(pattern, replace, content, flags=re.DOTALL)

def format_body(body, is_lexer=False):
    """
    Formats the body of a rule for W3C EBNF.
    """
    # Remove ANTLR actions if any
    body = re.sub(r'\{.*?\}', '', body, flags=re.DOTALL)

    # Remove lexer commands
    body = re.sub(r'->\s*\w+(\(.*?\))?', '', body)

    # Handle case-insensitive character classes in lexer rules
    if is_lexer:
        body = convert_char_classes(body)

    # Remove non-greedy markers
    body = body.replace('*?', '*').replace('+?', '+').replace('??', '?')

    # Clean up whitespace
    body = body.replace('\n', ' ').strip()
    body = re.sub(r'\s+', ' ', body)

    return body

def convert_char_classes(body):
    """
    Converts sequences like [tT][aA][bB] to 'TAB'.
    """
    def replace_sequence(match):
        chars = re.findall(r'\[([a-zA-Z])([a-zA-Z])\]', match.group(0))
        res = "".join(c1.upper() for c1, c2 in chars if c1.lower() == c2.lower())
        return f"'{res}'"

    return re.sub(r'(\[([a-zA-Z])([a-zA-Z])\])+', replace_sequence, body)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        content = sys.stdin.read()
    else:
        with open(sys.argv[1], 'r') as f:
            content = f.read()

    print(convert_antlr_to_ebnf(content))
