import os
import re
import sys

# Keywords that start a WebFOCUS block
START_KEYWORDS_FEX = [
    r'TABLE\s+FILE',
    r'DEFINE\s+FILE',
    r'GRAPH\s+FILE',
    r'MATCH\s+FILE',
    r'MAINTAIN\s+FILE',
    r'FILTER\s+FILE',
    r'CHECK\s+FILE',
    r'JOIN\s+',
]

# Case-sensitive start pattern for most code examples
START_PATTERN_FEX = re.compile(r'^\s*(?:\d+\.\s+)?(?:' + '|'.join(START_KEYWORDS_FEX) + r')')
# End pattern
END_PATTERN = re.compile(r'^\s*(?:\d+\.\s+)?END\s*$')

def is_mostly_code(line):
    """Heuristic to determine if a line is likely code vs prose."""
    stripped = line.strip()
    if not stripped: return False
    # Avoid TOC entries with dots
    if ' . . . ' in stripped or '...' in stripped: return False
    # Avoid lines ending in punctuation common for prose
    if stripped.endswith(',') or stripped.endswith('.'):
        # But allow it if it's a very short line or looks like a FEX command (e.g. "ON TABLE SUMMARIZE.")
        # though FEX usually doesn't end with a period.
        if len(stripped) > 20:
             return False

    # Check uppercase vs lowercase
    letters = re.sub(r'[^a-zA-Z]', '', stripped)
    if not letters: return True # Could be numbers/symbols code

    uppercase_count = sum(1 for c in letters if c.isupper())
    # If more than 50% is uppercase, it's likely code in this context
    return uppercase_count / len(letters) > 0.5

def fence_fex(content, filepath):
    # Skip Index and Front Matter
    filename = os.path.basename(filepath).lower()
    if 'appendix_d' in filename or 'front_matter' in filename:
        return content

    # Avoid double fencing
    if '```fex' in content:
        return content

    lines = content.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if START_PATTERN_FEX.match(line) and is_mostly_code(line):
            # Potential block start
            block_lines = [line]
            found_end = False

            # Look ahead for END
            for j in range(i + 1, min(i + 50, len(lines))):
                next_line = lines[j]
                block_lines.append(next_line)
                if END_PATTERN.match(next_line):
                    found_end = True
                    # Check if it's really a block or just a coincidence
                    # We look for other FEX-like lines in between
                    fex_indicators = ["BY ", "SUM ", "PRINT ", "WHERE ", "ON ", "HEADING ", "FOOTING ", "AND ", "SET "]
                    has_indicator = any(any(ind in l.upper() for ind in fex_indicators) for l in block_lines)

                    if found_end and (has_indicator or len(block_lines) > 2):
                        new_lines.append('```fex')
                        new_lines.extend(block_lines)
                        new_lines.append('```')
                        i = j + 1
                        break
                    else:
                        # Not a strong enough block, just add current line and continue
                        new_lines.append(line)
                        i += 1
                        break

                # If we hit another START before an END, this might be a one-liner or a malformed block
                if START_PATTERN_FEX.match(next_line):
                    # Check if current line is a known one-liner
                    if re.match(r'^\s*(?:\d+\.\s+)?(?:JOIN|CHECK|SQL)\s+', line, re.I):
                        new_lines.append('```fex')
                        new_lines.append(line)
                        new_lines.append('```')
                        i += 1
                        break
                    else:
                        # Just add it and continue
                        new_lines.append(line)
                        i += 1
                        break
            else:
                # No END found within 50 lines
                # Check if it's a known one-liner on a standalone line
                if re.match(r'^\s*(?:\d+\.\s+)?(?:JOIN|CHECK)\s+', line, re.I) and (i == 0 or not lines[i-1].strip()) and (i == len(lines)-1 or not lines[i+1].strip()):
                    new_lines.append('```fex')
                    new_lines.append(line)
                    new_lines.append('```')
                    i += 1
                else:
                    new_lines.append(line)
                    i += 1
            continue

        new_lines.append(line)
        i += 1

    return '\n'.join(new_lines)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = fence_fex(content, filepath)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    spec_root = 'specifications'
    files_changed = 0

    for root, dirs, files in os.walk(spec_root):
        for file in files:
            if file.endswith('.md') and file != 'ROADMAP.md':
                filepath = os.path.join(root, file)
                if process_file(filepath):
                    files_changed += 1
                    print(f"Fenced code blocks in: {filepath}")

    print(f"Total files changed: {files_changed}")

if __name__ == "__main__":
    main()
