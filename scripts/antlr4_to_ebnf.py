import re
import sys

def convert_antlr_to_ebnf(antlr_content):
    """
    Converts ANTLR4 grammar content to W3C EBNF.
    """
    # Rule regex that handles strings correctly.
    # It matches (optional fragment) name : body ;
    # body can contain strings '...' or "..." or any character except ;
    # We use a non-greedy match for the body but ensure it consumes full strings.
    rule_regex = r'(?m)^\s*(fragment\s+)?([a-zA-Z]\w*)\s*:\s*((?:\'(?:\'\'|[^\'])*\'|"(?:\"\"|[^\"])*"|[^;])+)\s*;'

    ebnf_rules = []

    for match in re.finditer(rule_regex, antlr_content):
        fragment, name, body = match.groups()
        start_pos = match.start()

        # Search for tags in the comments before this rule
        prev_content = antlr_content[:start_pos]
        last_semi = prev_content.rfind(';')
        if last_semi == -1:
            search_window = prev_content
        else:
            search_window = prev_content[last_semi:]

        tags = re.findall(r'@\w+', search_window)

        body = format_body(body, is_lexer=name[0].isupper())

        tag_prefix = ""
        if tags:
            tag_prefix = "[" + ",".join(t[1:] for t in tags) + "] "

        ebnf_rules.append(f"{tag_prefix}{name} ::= {body}")

    return "\n".join(ebnf_rules)

def format_body(body, is_lexer=False):
    """
    Formats the body of a rule for W3C EBNF.
    """
    # Remove ANTLR actions if any
    # Using a simple non-nested approach for now as it's common in these grammars
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
