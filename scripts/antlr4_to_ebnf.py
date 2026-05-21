import re
import sys

class Rule:
    def __init__(self, name, body, tags, description="", is_fragment=False, is_lexer=False, category=None, examples=None, used_by=None):
        self.name = name
        self.body = body
        self.tags = tags
        self.description = description
        self.is_fragment = is_fragment
        self.is_lexer = is_lexer
        self.category = category
        self.examples = examples or []
        self.used_by = used_by or []

def convert_antlr_to_ebnf(antlr_content):
    """
    Converts ANTLR4 grammar content to W3C EBNF with pruning and inlining.
    """
    # Rule regex that handles strings correctly.
    rule_regex = r'(?m)^\s*(fragment\s+)?([a-zA-Z]\w*)\s*:\s*((?:\'(?:\'\'|[^\'])*\'|"(?:\"\"|[^\"])*"|[^;])+)\s*;'


    rules = {}

    # 1. Extraction
    last_end = 0
    for match in re.finditer(rule_regex, antlr_content):
        fragment, name, body = match.groups()
        start_pos = match.start()

        # Search for tags and descriptions in the comments before this rule
        # We look back to the previous rule's end or start of file.
        search_window = antlr_content[last_end:start_pos]
        last_end = match.end()

        # Extract all comments in the search window to look for tags
        comments_list = re.findall(r'/\*.*?\*/|//[^\r\n]*', search_window, re.DOTALL)

        # Pre-process comments to extract tags and examples
        tags = []
        category = None
        examples = []

        for comment in comments_list:
            if comment.startswith('//'):
                content = comment[2:]
            else:
                content = comment[2:-2]

            # Clean up content (remove leading *)
            lines = [line.strip().lstrip('*').strip() for line in content.split('\n')]
            clean_content = "\n".join(lines)

            tags.extend([t[1:] for t in re.findall(r'@\w+', clean_content)])

            # Remove tags from description extraction by cleaning them out
            tag_free_content = re.sub(r'@\w+(\s+[^\r\n]*)?', '', clean_content).strip()

            cat_match = re.search(r'@category\s+([^\r\n]+)', clean_content)
            if cat_match and not category:
                category = cat_match.group(1).strip()

            examples.extend([m.group(1).strip() for m in re.finditer(r'@example\s+([^\r\n]+)', clean_content)])

        # Extract description (all comments that are not tags)
        description_lines = []
        for comment in comments_list:
            if comment.startswith('//'):
                content = comment[2:]
            else:
                content = comment[2:-2]

            lines = [line.strip().lstrip('*').strip() for line in content.split('\n')]
            for line in lines:
                # Skip lines that are just tags
                if not line or re.match(r'^\s*@\w+(\s+[^\r\n]*)?$', line):
                    continue
                # Clean tags from lines that might have them and other text (though unlikely)
                clean_line = re.sub(r'@\w+(\s+[^\r\n]*)?', '', line).strip()
                if clean_line:
                    description_lines.append(clean_line)

        description = "\n".join(description_lines).strip()

        is_lexer = name[0].isupper()
        body = format_body(body, is_lexer=is_lexer)

        rules[name] = Rule(name, body, tags, description=description, is_fragment=bool(fragment), is_lexer=is_lexer, category=category, examples=examples)

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

    # Add dummy rules for any character placeholders
    # W3C EBNF uses single quotes for terminals.
    # Note: These are technical lexer rules, better to just name them or use a safer terminal.
    rules['ANY_CHAR_EXCEPT_NL'] = Rule('ANY_CHAR_EXCEPT_NL', "'ANY_CHAR_EXCEPT_NL'", [], is_lexer=True)
    rules['ANY_CHAR_EXCEPT_QUOTE'] = Rule('ANY_CHAR_EXCEPT_QUOTE', "'ANY_CHAR_EXCEPT_QUOTE'", [], is_lexer=True)
    rules['ANY_CHAR_EXCEPT_DOUBLE_QUOTE'] = Rule('ANY_CHAR_EXCEPT_DOUBLE_QUOTE', "'ANY_CHAR_EXCEPT_DOUBLE_QUOTE'", [], is_lexer=True)

    # Multi-pass character exclusion replacement
    for name, rule in rules.items():
        body = rule.body
        # Handle MasterFile.g4 style STRING: '\'' ~'\''* '\'' | '"' ~'"'* '"'
        body = body.replace(r"~'\''", " ANY_CHAR_EXCEPT_QUOTE ")
        body = body.replace(r"~'", " ANY_CHAR_EXCEPT_QUOTE ")
        body = body.replace(r'~"', " ANY_CHAR_EXCEPT_DOUBLE_QUOTE ")
        rule.body = body

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

    # 3. Back-references calculation
    final_names = []
    for name, rule in rules.items():
        if name in actually_inlined:
            continue
        if (name in to_inline) and not re.search(rf'\b{name}\b', rule.body):
            continue
        final_names.append(name)

    for name in final_names:
        pattern = re.compile(rf'\b{name}\b')
        for other_name in final_names:
            if name == other_name:
                continue
            if pattern.search(rules[other_name].body):
                rules[name].used_by.append(other_name)

    # 4. Final Formatting
    ebnf_rules = []
    for name in final_names:
        rule = rules[name]
        ebnf_rules.append(f"{name} ::= {rule.body}")

    return "\n".join(ebnf_rules), rules

def check_coverage(antlr_content, ebnf_content):
    """
    Checks if all non-internal/non-inlined rules are present in the EBNF output.
    Returns a list of missing rules.
    """
    rule_regex = r'(?m)^\s*(fragment\s+)?([a-zA-Z]\w*)\s*:'

    # Extract rule names and their tags from ANTLR
    rules_metadata = {}
    for match in re.finditer(rule_regex, antlr_content):
        name = match.group(2)
        start_pos = match.start()

        prev_content = antlr_content[:start_pos]
        last_semi = prev_content.rfind(';')
        search_window = prev_content[last_semi:] if last_semi != -1 else prev_content
        tags = [t[1:] for t in re.findall(r'@\w+', search_window)]

        rules_metadata[name] = tags

    # Extract rule names from EBNF
    ebnf_rule_names = set(re.findall(r'^(\w+)\s*::=', ebnf_content, re.MULTILINE))

    missing = []
    for name, tags in rules_metadata.items():
        if 'internal' in tags or 'inline' in tags:
            continue
        if name not in ebnf_rule_names:
            missing.append(name)

    return missing

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

    # W3C EBNF doesn't support ~ (not) in all versions/tools, RR tool specifically struggles with it if not well-formed
    # For railroad diagrams, we can simplify this.

    # RR tool seems to have issues with backslash escapes for single quotes
    body = body.replace("\\'", "''")

    # Simple replacement for common patterns to make it more compatible
    body = re.sub(r'~\s*\[\\r\\n\]\*', ' ANY_CHAR_EXCEPT_NL* ', body)
    body = re.sub(r"~\s*\[\'\]\*", ' ANY_CHAR_EXCEPT_QUOTE* ', body)
    body = re.sub(r'~\s*\["\]\*', ' ANY_CHAR_EXCEPT_DOUBLE_QUOTE* ', body)

    # MasterFile special cases in lexer
    body = body.replace("~'\\''*", " ANY_CHAR_EXCEPT_QUOTE* ")
    body = body.replace('~"\'\'*', " ANY_CHAR_EXCEPT_DOUBLE_QUOTE* ")
    body = body.replace('~"\'*', " ANY_CHAR_EXCEPT_DOUBLE_QUOTE* ")
    body = body.replace("~'\\''", " ANY_CHAR_EXCEPT_QUOTE ")
    body = body.replace('~"', " ANY_CHAR_EXCEPT_DOUBLE_QUOTE ")

    body = body.replace('~', 'NOT ')

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
    import argparse
    import json
    parser = argparse.ArgumentParser(description='Convert ANTLR4 to W3C EBNF')
    parser.add_argument('input', nargs='?', help='Input ANTLR4 file')
    parser.add_argument('--check', action='store_true', help='Check grammar coverage')
    parser.add_argument('--metadata', help='Output metadata (rule descriptions) to this JSON file')

    args = parser.parse_args()

    if args.input:
        with open(args.input, 'r') as f:
            content = f.read()
    else:
        content = sys.stdin.read()

    ebnf, rules = convert_antlr_to_ebnf(content)

    if args.metadata:
        metadata = {
            name: {
                "description": rule.description,
                "category": rule.category,
                "examples": rule.examples,
                "used_by": rule.used_by
            } for name, rule in rules.items() if rule.description or rule.category or rule.examples or rule.used_by
        }
        with open(args.metadata, 'w') as f:
            json.dump(metadata, f, indent=2)

    if args.check:
        missing = check_coverage(content, ebnf)
        if missing:
            print(f"Error: Missing rules in EBNF output: {', '.join(missing)}", file=sys.stderr)
            sys.exit(1)
        else:
            print("Coverage check passed.", file=sys.stderr)

    print(ebnf)
