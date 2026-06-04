import os
import re
import sys

DM_COMMANDS = [
    '-SET', '-DEFAULTH', '-DEFAULT', '-RUN', '-INCLUDE', '-HTMLFORM',
    '-TYPE', '-GOTO', '-IF', '-REPEAT', '-EXIT', '-QUIT', '-OLAP', '-MRNOEDIT'
]

SQL_COMMANDS = [
    'SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'DROP', 'ALTER'
]

def is_dm_start(line):
    stripped = line.strip().upper()
    if not stripped.startswith('-'):
        return False
    for cmd in DM_COMMANDS:
        if stripped.startswith(cmd):
            return True
    return False

def is_sql_start(line):
    stripped = line.strip().upper()

    # Stricter SQL start detection
    if stripped.startswith('SELECT A ') or stripped.startswith('SELECT THE ') or stripped.startswith('SELECT FROM '):
        return False

    # Check if the line is likely prose (mixed case with many lower case letters)
    lower_count = sum(1 for c in line if c.islower())
    if lower_count > 5:
        # If it has many lowercase letters, it's likely prose unless it's a very specific code pattern
        # But SQL in these docs is almost always uppercase
        if not (stripped.startswith('SELECT ') and ' FROM ' in stripped):
            return False

    for cmd in SQL_COMMANDS:
        if stripped.startswith(cmd + ' ') or stripped == cmd:
            return True

    # Special case for WITH - must look like code
    if stripped.startswith('WITH ') and ' AS ' in stripped and '(' in stripped:
        return True

    return False

def is_dm_line(line):
    s = line.strip().upper()
    if not s: return True
    if s.startswith('-'): return True
    if any(s.startswith(c) for c in ['SUM ', 'BY ', 'PRINT ', 'TABLE FILE ', 'END', 'SET ', 'ON TABLE ', 'WHERE ']):
        return True
    if line.startswith('   '): # Indented continuation
        return True
    return False

def is_sql_line(line):
    s = line.strip().upper()
    if not s: return True
    # If it's a header or list item, it's not SQL code
    if s.startswith('#') or s.startswith('* ') or s.startswith('- '):
        return False
    # If it ends in a period and has significant lowercase, it's likely prose
    if line.strip().endswith('.') and sum(1 for c in line if c.islower()) > 5:
        # But allow it if it's a single word line that happens to end in a dot (unlikely but safe)
        if len(line.split()) > 2:
            return False
    return True

def fence_blocks(content):
    lines = content.split('\n')
    new_lines = []
    i = 0
    in_markdown_fence = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith('```'):
            in_markdown_fence = not in_markdown_fence
            new_lines.append(line)
            i += 1
            continue

        if in_markdown_fence:
            new_lines.append(line)
            i += 1
            continue

        # 1. TABLE FILE / GRAPH FILE blocks
        if stripped.upper().startswith('TABLE FILE') or stripped.upper().startswith('GRAPH FILE'):
            found_end = -1
            for j in range(i, min(i + 100, len(lines))):
                if lines[j].strip().startswith('```'):
                    break
                if lines[j].strip().upper() == 'END':
                    found_end = j
                    break

            if found_end != -1:
                if new_lines and new_lines[-1].strip():
                    new_lines.append('')
                new_lines.append('```fex')
                for k in range(i, found_end + 1):
                    new_lines.append(lines[k])
                new_lines.append('```')
                if found_end + 1 < len(lines) and lines[found_end + 1].strip():
                    new_lines.append('')
                i = found_end + 1
                continue

        # 2. Dialogue Manager blocks
        if is_dm_start(line):
            block_end = i
            for j in range(i, min(i + 50, len(lines))):
                if lines[j].strip().startswith('```'):
                    break
                if not is_dm_line(lines[j]):
                    break
                # Allow up to 2 blank lines if followed by more code
                if not lines[j].strip():
                    follow_up = False
                    for k in range(j + 1, min(j + 3, len(lines))):
                        if lines[k].strip() and is_dm_line(lines[k]):
                            follow_up = True
                            break
                    if not follow_up:
                        break
                block_end = j

            if block_end >= i:
                if new_lines and new_lines[-1].strip():
                    new_lines.append('')
                new_lines.append('```fex')
                for k in range(i, block_end + 1):
                    new_lines.append(lines[k])
                new_lines.append('```')
                if block_end + 1 < len(lines) and lines[block_end + 1].strip():
                    new_lines.append('')
                i = block_end + 1
                continue

        # 3. SQL blocks
        if is_sql_start(line):
            has_from = False
            block_end = i
            for j in range(i, min(i + 50, len(lines))):
                if lines[j].strip().startswith('```'):
                    break
                if not is_sql_line(lines[j]):
                    break
                # Allow up to 2 blank lines if followed by more code
                if not lines[j].strip():
                    follow_up = False
                    for k in range(j + 1, min(j + 3, len(lines))):
                        if lines[k].strip() and is_sql_line(lines[k]):
                            follow_up = True
                            break
                    if not follow_up:
                        break
                if ' FROM ' in lines[j].upper():
                    has_from = True
                block_end = j

            if has_from:
                if new_lines and new_lines[-1].strip():
                    new_lines.append('')
                new_lines.append('```sql')
                for k in range(i, block_end + 1):
                    new_lines.append(lines[k])
                new_lines.append('```')
                if block_end + 1 < len(lines) and lines[block_end + 1].strip():
                    new_lines.append('')
                i = block_end + 1
                continue

        new_lines.append(line)
        i += 1

    return '\n'.join(new_lines)

def process_file(filepath):
    if not os.path.isfile(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = fence_blocks(content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    spec_root = 'specifications'
    files_processed = 0
    files_changed = 0

    if len(sys.argv) > 1:
        targets = sys.argv[1:]
    else:
        targets = []
        spec_dirs = ['creating_reports', 'describing_data']
        for sd in spec_dirs:
            full_sd = os.path.join(spec_root, sd)
            if os.path.isdir(full_sd):
                for filename in sorted(os.listdir(full_sd)):
                    if filename.endswith('.md'):
                        targets.append(os.path.join(full_sd, filename))

    for filepath in targets:
        files_processed += 1
        if process_file(filepath):
            files_changed += 1
            print(f"Fenced code blocks in: {filepath}")

    print(f"Processed {files_processed} files, changed {files_changed}.")

if __name__ == "__main__":
    main()
