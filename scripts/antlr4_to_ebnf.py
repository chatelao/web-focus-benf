import re
import sys

class Rule:
    def __init__(self, name, body, tags, is_fragment=False, is_lexer=False):
        self.name = name
        self.body = body
        self.tags = tags
        self.is_fragment = is_fragment
        self.is_lexer = is_lexer

def convert_antlr_to_ebnf(antlr_content):
    """
    Converts ANTLR4 grammar content to W3C EBNF with pruning and inlining.
    """
    # Rule regex that handles strings correctly.
    rule_regex = r'(?m)^\s*(fragment\s+)?([a-zA-Z]\w*)\s*:\s*((?:\'(?:\'\'|[^\'])*\'|"(?:\"\"|[^\"])*"|[^;])+)\s*;'

    rules = {}

    # 1. Extraction
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

        tags = [t[1:] for t in re.findall(r'@\w+', search_window)]

        is_lexer = name[0].isupper()
        body = format_body(body, is_lexer=is_lexer)

        rules[name] = Rule(name, body, tags, is_fragment=bool(fragment), is_lexer=is_lexer)

    # 2. Inlining
    to_inline = [name for name, rule in rules.items() if 'inline' in rule.tags or 'internal' in rule.tags]
    actually_inlined = set()

    # Pre-wrap bodies of rules that will be inlined if they are complex
    for name in to_inline:
        rule = rules[name]
        body = rule.body.strip()
        # Direct recursion check for pre-wrapping
        if re.search(rf'\b{name}\b', body):
            continue

        if ' ' in body or '|' in body:
            if not (body.startswith('(') and body.endswith(')')):
                rule.body = f"( {body} )"

    # Multiple passes to handle nested inlining
    max_passes = 10
    for _ in range(max_passes):
        any_changed = False
        for name_to_inline in to_inline:
            rule_to_inline = rules[name_to_inline]
            inline_body = rule_to_inline.body

            # If name_to_inline appears in its own body, we have direct recursion.
            # Inlining it would be infinite.
            if re.search(rf'\b{name_to_inline}\b', inline_body):
                continue

            pattern = re.compile(rf'\b{name_to_inline}\b')
            for name, rule in rules.items():
                if name == name_to_inline:
                    continue

                # Using a lambda for replacement to avoid backslash escaping issues in re.sub
                new_body = pattern.sub(lambda m: inline_body, rule.body)
                if new_body != rule.body:
                    rule.body = new_body
                    any_changed = True
                    actually_inlined.add(name_to_inline)
        if not any_changed:
            break

    # 3. Final Formatting
    ebnf_rules = []
    for name, rule in rules.items():
        # A rule is removed if it was successfully inlined into something else,
        # OR if it was tagged for inlining/pruning and is NOT recursive (safe to remove).
        if name in actually_inlined:
            continue
        if (name in to_inline) and not re.search(rf'\b{name}\b', rule.body):
            continue

        ebnf_rules.append(f"{name} ::= {rule.body}")

    return "\n".join(ebnf_rules)

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
