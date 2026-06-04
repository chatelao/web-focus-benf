import os
import re
import sys

def fence_webfocus_blocks(content):
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

        if not in_markdown_fence and (stripped.upper().startswith('TABLE FILE') or stripped.upper().startswith('GRAPH FILE')):
            # Potential start of a block
            # Look ahead for END
            found_end = -1
            # We search up to 50 lines ahead to avoid consuming too much if END is missing
            for j in range(i, min(i + 50, len(lines))):
                if lines[j].strip().startswith('```'): # Don't cross existing fences
                    break
                if lines[j].strip().upper() == 'END':
                    found_end = j
                    break

            if found_end != -1:
                # We found a block!
                # If the previous line isn't empty, add an empty line for better Markdown formatting
                if new_lines and new_lines[-1].strip():
                    new_lines.append('')

                new_lines.append('```fex')
                for k in range(i, found_end + 1):
                    new_lines.append(lines[k])
                new_lines.append('```')

                # If the next line isn't empty, add an empty line after the fence
                if found_end + 1 < len(lines) and lines[found_end + 1].strip():
                    new_lines.append('')

                i = found_end + 1
                continue

        new_lines.append(line)
        i += 1

    return '\n'.join(new_lines)

def process_file(filepath):
    if not os.path.isfile(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = fence_webfocus_blocks(content)

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
