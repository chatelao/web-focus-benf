import os
import re
import sys

def standardize_sections(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        return False

    # Find the "In this chapter:" or "In this appendix:" block
    start_index = -1
    for i, line in enumerate(lines):
        if re.search(r'In this (chapter|appendix):', line, re.IGNORECASE):
            start_index = i
            break

    if start_index == -1:
        return False

    # Extract titles
    titles = []
    i = start_index + 1
    # Skip initial blank lines
    while i < len(lines) and not lines[i].strip():
        i += 1

    list_end_index = -1
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue

        # If we see a title that is already in the list, it's probably the start of the sections
        if stripped in titles:
            list_end_index = i
            break

        # If it's a long line, it's probably not a title
        if len(stripped) > 100:
            list_end_index = i
            break

        titles.append(stripped)
        i += 1

    if not titles:
        return False

    # Now we have the titles. We want to find them in the rest of the file.
    search_start = list_end_index if list_end_index != -1 else i

    new_lines = lines[:search_start]
    changed = False

    # We want to match titles only if they are on a line by themselves
    # (allowing for leading/trailing whitespace)
    # AND they are not already headers.

    last_converted_title = None

    for i in range(search_start, len(lines)):
        line = lines[i]
        stripped = line.strip()

        if stripped in titles:
            # Check if it's already a header
            if not line.startswith('#'):
                # Check if the title is on a line by itself (ignoring whitespace)
                # and NOT part of another sentence.
                # Since we used lines[i].strip(), we know the line ONLY contains the title.

                # Heuristic: Avoid converting if it's the exact same as the last line we converted
                if stripped == last_converted_title:
                    # Skip this one, it's likely a duplicate artifact
                    changed = True
                    continue

                # Heuristic: Only convert if the previous non-empty line was empty or a header
                # and the next non-empty line is not just the same title again.

                new_lines.append(f"## {stripped}\n")
                last_converted_title = stripped
                changed = True
                continue

        new_lines.append(line)
        if stripped:
            if stripped in titles and line.startswith('#'):
                last_converted_title = stripped
            else:
                last_converted_title = None

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    return False

def main():
    spec_root = 'specifications'
    files_processed = 0
    files_changed = 0

    spec_dirs = ['creating_reports', 'describing_data']
    for sd in spec_dirs:
        full_sd = os.path.join(spec_root, sd)
        if os.path.isdir(full_sd):
            for filename in sorted(os.listdir(full_sd)):
                if filename.endswith('.md') and ('chapter' in filename or 'appendix' in filename):
                    filepath = os.path.join(full_sd, filename)
                    files_processed += 1
                    if standardize_sections(filepath):
                        files_changed += 1
                        print(f"Standardized sections in: {filepath}")

    print(f"Processed {files_processed} files, changed {files_changed}.")

if __name__ == "__main__":
    main()
